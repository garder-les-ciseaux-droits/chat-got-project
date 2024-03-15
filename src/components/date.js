const text = 'Hello How are you?';
const array = text.split('');

function delayedReturn(index) {
    return new Promise(resolve => {
        setTimeout(() => {
            resolve(array[index]);
        }, 1000);
    });
}

async function processArray() {
    for (let i = 0; i < array.length; i++) {
        const result = await delayedReturn(i);
        return result; // Здесь вы можете использовать возвращенное значение
    }
}

processArray();
