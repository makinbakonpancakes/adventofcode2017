function inverse_captcha(data, shift) {
    return data.filter((n, i, a) => n === a[(i + shift) % a.length])
               .reduce((sum, n) => sum + n, 0);
}

const data = [...document.getElementById("input").textContent.trim()].map(Number);
document.writeln();
document.writeln(inverse_captcha(data, 1));
document.writeln(inverse_captcha(data, data.length / 2));
