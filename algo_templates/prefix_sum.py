def build_prefix_sum(arr):
  n = len(arr)
  prefix_sum = [0] * n
  prefix_sum[0] = arr[0]
  for m in range(1, n):
    prefix_sum[m] = prefix_sum[m - 1] + arr[m]
  return prefix_sum

def query_range(prefix_sum, left, right):
  if left == 0:
    return prefix_sum[right]
  return prefix_sum[right] - prefix_sum[left - 1]
