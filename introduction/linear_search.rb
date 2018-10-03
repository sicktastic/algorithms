def linear_search(list, target)
  0.upto(list.length) do |i|
    if list[i] == target
      return i
    end
  end

  return nil
end

def return_test(i)
  return i
end

def verify(index)
  if index != nil
    puts "Target found at index: " + index.to_s
  else
    puts "Target not found in list"
  end
end

numbers = [1,2,3,4,5,6,7,8,9,10]

result = linear_search(numbers, 12)
verify(result)

result = linear_search(numbers, 6)
verify(result)

