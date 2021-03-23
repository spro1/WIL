def solution(participant, completion):
  answer = ''
  dic = {}

  for p in participant:
    if not (p in dic):
      dic[p] = 1
    else:
      dic[p] += 1

  arr = list(dic.keys())

  for c in completion:
    dic[c] -= 1

  ii = 0
  for i in dic.keys():
    if dic[i] != 0:
      answer = arr[ii]
      break
    ii += 1

  return answer
