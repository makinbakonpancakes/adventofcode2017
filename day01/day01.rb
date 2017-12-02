def inverse_captcha(data, shift)
  data.zip(data.rotate(shift))
    .select { |x| x[0] == x[1] }
    .reduce(0) { |s, i| s + i[0] }
end

data = File.read('input.txt').strip().chars.map {|x| Integer(x)}
puts inverse_captcha(data, 1)
puts inverse_captcha(data, data.length / 2)
