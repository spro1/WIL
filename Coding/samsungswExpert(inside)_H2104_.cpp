#define MAX_SIZE 300
#define MAX_LEN 12
#define MAX_CNT 5001
#define IDLE 0

int mstrcmp(const char *a, const char *b)
{
	int i;
	for (i = 0; a[i] != '\0'; i++)
	{
		if (a[i] != b[i])
			return a[i] - b[i];
	}
	return a[i] - b[i];
}

void mstrcpy(char *dest, const char *src)
{
	int i = 0;
	while (src[i] != '\0')
	{
		dest[i] = src[i];
		i++;
	}
	dest[i] = src[i];
}

unsigned long getHash(const char* str)
{
	unsigned long hash = 5381;
	int c;
	
	register int i = 0;
	while (c = *str++ && i < 6)
	{
		hash = (((hash << 5) + hash) + c) % MAX_CNT;
	}

	return hash % MAX_CNT;
}

unsigned long getHash(const char* str, int pos)
{
	unsigned long hash = 5381;
	int c;

	register int i = 0;
	while (c = *str++ && i < 6)
	{
		hash = (((hash << 5) + hash) + c) % MAX_CNT;
	}

	hash = ((hash << 5) + hash) + ('0' + pos) % MAX_CNT;

	return hash % MAX_CNT;
}

/////////////////////////////////////////////////////////////
typedef struct name {
	char name[MAX_LEN];
	int targetHash;
	int sizeR, sizeC;
	int posR, posC;
	struct name* otherName;
}NAME;
NAME gstNames[MAX_CNT];

typedef struct tag {
	char tag[MAX_LEN];
	NAME* nameHead;
}TAG;
TAG gstTags[MAX_CNT];

int container[MAX_SIZE][MAX_SIZE];
int integContainer[MAX_SIZE][MAX_SIZE];
int containerR, containerC;

void init(int R, int C) {
	register int i, j;

	containerR = R;
	containerC = C;

	for (i = 0; i < containerR; i++) {
		for (j = 0; j < containerC; j++) {
			container[i][j] = 0;
			integContainer[i][j] = 0;
		}
	}

	for (i = 0; i < MAX_CNT; i++) {		
		gstTags[i].tag[0] = '\0';
		gstTags[i].nameHead = nullptr;
		gstNames[i].name[0] = '\0';
		gstNames[i].otherName = nullptr;
	}
}

// mode 0: 삭제, mode 1: 할당
void editContainer(int r, int c, int h, int w, int mode) {
	register int i, j;
	for (i = c; i < c + w; i++) {
		for (j = r; j < r + h; j++) {
			container[j][i] = mode;
		}
	}

	for (i = c; i < containerC; i++) {
		for (j = r; j < containerR; j++) {
			if (i > 0 && j > 0) {
				integContainer[j][i] = integContainer[j][i - 1] + integContainer[j - 1][i] + container[j][i] - integContainer[j - 1][i - 1];
			}
			else {
				if (j == 0 && i == 0) {
					integContainer[j][i] = container[j][i];
				}
				else if (j == 0) {
					integContainer[j][i] = integContainer[j][i - 1] + container[j][i];
				}
				else if (i == 0) {
					integContainer[j][i] = integContainer[j - 1][i] + container[j][i];
				}
			}
		}
	}
}

bool existCheck(int r, int c, int h, int w) {
	/*for (int k = c + w; k >= c; k--) {
		for (int l = r + h; l >= r; l--) {
			if (container[l][k]) {
				return true;
			}
		}
	}*/

	int sumArea;

	if (r > 0 && c > 0) {
		sumArea = integContainer[r + h][c + w] - integContainer[r - 1][c + w] - integContainer[r + h][c - 1] + integContainer[r - 1][c - 1];
	}
	else {
		if (r == 0 && c == 0) {
			sumArea = integContainer[r + h][c + w];
		}
		else if (r == 0) {
			sumArea = integContainer[r + h][c + w] - integContainer[r + h][c - 1];
		}
		else if (c == 0) {
			sumArea = integContainer[r + h][c + w] - integContainer[r - 1][c + w];
		}
	}

	return sumArea;
}

bool searchContainer(int* posR, int* posC, int h, int w) {
	register int i, j;
	for (i = 0; i < containerC - w; i++) {
		for (j = 0; j < containerR - h; j++) {
			if (container[j][i] == 0 &&
				i + w <= containerC - 1 && j + h <= containerR - 1) 
			{
				if (!existCheck(j, i, h, w)) {
					*posR = j;
					*posC = i;

					return true;
				}
			}
		}
	}
	return false;
}

bool searchContainer(int* posR, int* posC, int h, int w, int r, int c) {
	int row = r - 1;
	int col = c - 1;

	if (col + w <= containerC - 1 && row + h <= containerR - 1) {
		if (!existCheck(row, col, h, w)) {
			*posR = row;
			*posC = col;

			return true;
		}
	}
	return false;
}

int addItem(char name[], char tag[], int height, int width, int mode, int r, int c) {
	int posR, posC;
	bool enableFlag;

	int h = height - 1;
	int w = width - 1;

	if(mode == 1) enableFlag = searchContainer(&posR, &posC, h, w);
	else enableFlag = searchContainer(&posR, &posC, h, w, r, c);

	if (enableFlag) {
		int hashTag = getHash(tag);
		int hashName = getHash(name);
		TAG*  psTag;
		NAME* psName;
		
 		while (!gstTags[hashTag].tag[0] == '\0' && mstrcmp(tag, gstTags[hashTag].tag)) {
			hashTag++;
		}
		while (!gstNames[hashName].name[0] == '\0' && mstrcmp(name, gstNames[hashName].name)) {
			hashName++;
		}

		psTag = &gstTags[hashTag];
		psName = &gstNames[hashName];
		mstrcpy(psName->name, name);
		psName->posR = posR;
		psName->posC = posC;
		psName->sizeR = height;
		psName->sizeC = width;
		psName->targetHash = hashTag;

		if (psTag->tag[0] == '\0') {
			mstrcpy(psTag->tag, tag);
		}

		if (!psTag->nameHead) {
			psTag->nameHead = psName;
		}
		else {
			NAME* tempName = psTag->nameHead;
			for (; tempName != nullptr; tempName = tempName->otherName) {
				if (!tempName->otherName) {
					tempName->otherName = psName;
					break;
				}
			}
		}

		editContainer(posR, posC, height, width, hashName);

		return 1;
	}
	else {
		return 0;
	}
}

int removeItemByName(char name[]) {
	int hashTag;
	int hashName = getHash(name);
	TAG* psTag;
	NAME* psName;
	NAME* tmpName;

	int cnt = 0;
	char ttName[100][11];
	while (mstrcmp(name, gstNames[hashName].name)) {
		if (gstNames[hashName].name[0] == '\0') {
			return 0;
		}
		hashName++;
	}

	psName = &gstNames[hashName];
	psTag = &gstTags[psName->targetHash];
	tmpName = psName = psTag->nameHead;

	while (psName != nullptr) {
		if (!mstrcmp(psName->name, name)) {
			break;
		}

		tmpName = psName;
		psName = psName->otherName;
	}
	
	if (psName == nullptr) {
		return 0;
	}

	editContainer(psName->posR, psName->posC, psName->sizeR, psName->sizeC, IDLE);

	psName->name[0] = '\0';

	if (psTag->nameHead == psName) {
		psTag->nameHead = psName->otherName;
	}
	else {
		tmpName->otherName = psName->otherName;
	}

	return 1;
}

int removeItemByTag(char tag[]) {
	int hashTag = getHash(tag);;
	int hashName;
	TAG* psTag;
	NAME* psName;

	int rmCnt = 0;

	while (mstrcmp(tag, gstTags[hashTag].tag)) {
		if (gstTags[hashTag].tag[0] == '\0') {
			return 0;
		}
		hashTag++;
	}

	psTag = &gstTags[hashTag];
	psName = psTag->nameHead;
	for (; psName != nullptr; psName = psName->otherName) {
		editContainer(psName->posR, psName->posC, psName->sizeR, psName->sizeC, IDLE);
		rmCnt++;
	}

	psTag->nameHead = nullptr;

	return rmCnt;
}

int getItem(int r, int c, char name[], char tag[]) {
	int hashTag;
	int hashName;
	TAG* psTag;
	NAME* psName;

	if (container[r - 1][c - 1]) {
		psName = &gstNames[container[r - 1][c - 1]];
		hashTag = psName->targetHash;
		psTag = &gstTags[hashTag];

		mstrcpy(name, psName->name);
		mstrcpy(tag, psTag->tag);

		return 1;
	}
	else {
		return 0;
	}
}

int getArea(char tag[]) {
	int hashTag = getHash(tag);;
	int hashName;
	TAG* psTag;
	NAME* psName;

	int size = 0;

	while (mstrcmp(tag, gstTags[hashTag].tag)) {
		if (gstTags[hashTag].tag[0] == '\0') {
			return 0;
		}

		hashTag++;
	}

	psTag = &gstTags[hashTag];
	psName = psTag->nameHead;
	for (; psName != nullptr; psName = psName->otherName) {
		size += psName->sizeR * psName->sizeC;
		// size += existCheck(psName->posR, psName->posC, psName->sizeR, psName->sizeC);
	}

	return size;
}