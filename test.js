let inputString = 'Hello, this is your script: `print(123)`. HII!';

// Используем регулярное выражение для извлечения текста внутри обратных кавычек
let regex = /`([^`]+)`/;
let match = inputString.match(regex);

// Если найдено совпадение, извлекаем текст из группы захвата
if (match) {
  let extractedCode = match[1];
  console.log(extractedCode);
} else {
  console.log("Совпадение не найдено");
}
