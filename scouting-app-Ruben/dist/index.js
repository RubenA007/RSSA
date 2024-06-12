//Страничные блоки по кнопкам(чек html файл)
//При нажатии на определенную кнопку, состояние блоков будет none- скрыто, block-видно
//Main
document.getElementById('Main-button').addEventListener('click', function () {
  document.getElementById('Main').style.display = 'block';
  document.getElementById('Autonomus').style.display = 'none';
  document.getElementById('Teleop').style.display = 'none';
  document.getElementById('End Game').style.display = 'none';
  document.getElementById('Penalty/information').style.display = 'none';

});
//Autonomus
document.getElementById('Autonomus-button').addEventListener('click', function () {
  document.getElementById('Main').style.display = 'none';
  document.getElementById('Autonomus').style.display = 'block';
  document.getElementById('Teleop').style.display = 'none';
  document.getElementById('End Game').style.display = 'none';
  document.getElementById('Penalty/information').style.display = 'none';

});
//Teleop
document.getElementById('Teleop-button').addEventListener('click', function () {
  document.getElementById('Main').style.display = 'none';
  document.getElementById('Autonomus').style.display = 'none';
  document.getElementById('Teleop').style.display = 'block';
  document.getElementById('End Game').style.display = 'none';
  document.getElementById('Penalty/information').style.display = 'none';

});
//End Game
document.getElementById('End Game-button').addEventListener('click', function () {
  document.getElementById('Main').style.display = 'none';
  document.getElementById('Autonomus').style.display = 'none';
  document.getElementById('Teleop').style.display = 'none';
  document.getElementById('End Game').style.display = 'block';
  document.getElementById('Penalty/information').style.display = 'none';

});
//Penalty/information
document.getElementById('Penalty/information-button').addEventListener('click', function () {
  document.getElementById('Main').style.display = 'none';
  document.getElementById('Autonomus').style.display = 'none';
  document.getElementById('Teleop').style.display = 'none';
  document.getElementById('End Game').style.display = 'none';
  document.getElementById('Penalty/information').style.display = 'block';

});

//Математические действия для счетчиков
// Увеличение счетчика на 1
function incrementCounter(counterNumber) {
  let counter = parseInt($('#counter' + counterNumber).text());
  counter++;

  $('#counter' + counterNumber).text(counter);


}

// Уменьшение счетчика на 1
function decrementCounter(counterNumber) {
  let counter = parseInt($('#counter' + counterNumber).text());
  counter--;

  $('#counter' + counterNumber).text(counter);


}

//Функция для Ресета или же обнуления значений
function Reset() {

  document.getElementById('id').value = "";
  document.getElementById('information').value = "";

  document.getElementById('counter1').innerHTML = 0;
  document.getElementById('counter2').innerHTML = 0;
  document.getElementById('counter3').innerHTML = 0;
  document.getElementById('counter4').innerHTML = 0;
  document.getElementById('counter5').innerHTML = 0;
  document.getElementById('counter6').innerHTML = 0;
  document.getElementById('counter7').innerHTML = 0;
  document.getElementById('counter8').innerHTML = 0;
  document.getElementById('counter9').innerHTML = 0;
  document.getElementById('counter10').innerHTML = 0;
  document.getElementById('counter11').innerHTML = 0;
  document.getElementById('counter12').innerHTML = 0;
  document.getElementById('counter13').innerHTML = 0;
  document.getElementById('counter14').innerHTML = 0;
  document.getElementById('counter15').innerHTML = 0;
  document.getElementById('counter16').innerHTML = 0;
  document.getElementById('counter17').innerHTML = 0;
  document.getElementById('counter18').innerHTML = 0;
  document.getElementById('counter19').innerHTML = 0;
  //По идее, при ресете, кол-во строк должно сброситься до 1, но это работает при нажатии после ресета
  if (document.getElementById('id').value == "") {
    document.getElementById('id').rows = 1;
  }
}
/*При написании текста в infromation текстовое поле будет увеличиваться. 
У поля есть определенная длина и 1 строка с самого начала
Если длина строки не вмещается и она больше 1, то +1 строка*/
var tx = document.getElementsByTagName('textarea');
for (var i = 1; i < tx.length; i++) {
  tx[i].setAttribute('style', 'height:' + (tx[i].scrollHeight) + 'px;overflow-y:hidden;');
  tx[i].addEventListener("input", OnInput, false);
}

function OnInput() {
  this.style.height = 'auto';
  this.style.height = (this.scrollHeight) + 'px'
}



//Показ списка
function show() {
  document.getElementById('showOverlay').addEventListener('click', function () {
    document.getElementById('overlay').style.display = 'flex';
  });
}
//При нажатии на кнопку, список скрывается
var overlayButtons = document.getElementsByClassName('overlayButton');
for (var i = 0; i < overlayButtons.length; i++) {
  overlayButtons[i].addEventListener('click', function () {
    document.getElementById('overlay').style.display = 'none';
  });
}

/*На данный момент работает только с ответами*/


  /*
  const scriptURL = 'https://script.google.com/macros/s/AKfycbwR3UUQr5gqOUfEla4KsaTVZ92YWIl_6ZoHFlDurx0IYnDe1GXhrfODCwCzzk09YK0/exec'
  const form = document.forms['submit-to-google-sheet']

  form.addEventListener('submit', e => {
    e.preventDefault()
    fetch(scriptURL, { method: 'POST', body: new FormData(form) })
      .then(response => console.log('Success!', response))
      .catch(error => console.error('Error!', error.message))
  })
*/
function Send() {
    var counter1Value = document.getElementById('counter1').value;
    var counter19Value = document.getElementById('counter19').value;
    var counter2Value = document.getElementById('counter2').value;
    var counter3Value = document.getElementById('counter3').value;
    var counter4Value = document.getElementById('counter4').value;
    var counter5Value = document.getElementById('counter5').value;
    var counter6Value = document.getElementById('counter6').value;
    var counter7Value = document.getElementById('counter7').value;
    var counter8Value = document.getElementById('counter8').value;
    var counter9Value = document.getElementById('counter9').value;
    var counter10Value = document.getElementById('counter10').value;
    var counter11Value = document.getElementById('counter11').value;
    var counter12Value = document.getElementById('counter12').value;
    var counter13Value = document.getElementById('counter13').value;
    var counter14Value = document.getElementById('counter14').value;
    var counter15Value = document.getElementById('counter15').value;
    var counter16Value = document.getElementById('counter16').value;
    var counter17Value = document.getElementById('counter17').value;
    var counter18Value = document.getElementById('counter18').value;

    var id = document.getElementById('id').value;
    var information = document.getElementById('information').value;

    var data = {
      id: id,
      information: information,
      counter1Value: counter1Value,
      counter19Value: counter19Value,
      counter2Value: counter2Value,
      counter3Value: counter3Value,
      counter4Value: counter4Value,
      counter5Value: counter5Value,
      counter6Value: counter6Value,
      counter7Value: counter7Value,
      counter8Value: counter8Value,
      counter9Value: counter9Value,
      counter10Value: counter10Value,
      counter11Value: counter11Value,
      counter12Value: counter12Value,
      counter13Value: counter13Value,
      counter14Value: counter14Value,
      counter15Value: counter15Value,
      counter16Value: counter16Value,
      counter17Value: counter17Value,
      counter18Value: counter18Value,
    }
    const scriptURL = 'https://script.google.com/macros/s/AKfycbwR3UUQr5gqOUfEla4KsaTVZ92YWIl_6ZoHFlDurx0IYnDe1GXhrfODCwCzzk09YK0/exec'
const form = document.forms['submit-to-google-sheet']
form.addEventListener('submit', e => {
  e.preventDefault()  
  fetch(scriptURL, {
      method: 'POST',
      body: JSON.stringify(data)
    })
    .then(response => {
      console.log('Данные успешно отправлены');
    })
    .catch(error => {
      console.error('Ошибка:', error)
    })
})
}










