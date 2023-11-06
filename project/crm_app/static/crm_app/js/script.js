//console.log('hello world!');
//console.log('вучым ' + ' js');
//let = 'django';
//console.log(let + " is my passion");
///*comments  */
//function name() {
//    console.log('yes yes yes');
//    }
//
//name();
//
//let textColor = 'red';
//let age = 25;
//textColor= 'blue';
//
///*alert(textColor);*/
//const doc = 'tn';
//for (let i=0; i<5; i++){
//    console.log(doc+i);
//    }
//
//
//let block = document.querySelector('.block');
//console.log(block);
//console.log(typeof block);
//let obratnyeKavychki = `обратные кавычки и возраст: ${age}`;
//console.log(obratnyeKavychki);
////object:
//let myInfo = {
//    name: "liuba",
//    surname: "kovaleva"
//};
//
//console.log(myInfo);
//console.log(typeof myInfo);
//
////changing typeof:
//newage = String(age);
//console.log(typeof newage);
//
//// or ||
//console.log(true || false);
//// &&
//console.log(true && true);
//// && > ||
//
//console.log(!true);
//
////сравнение с null:  сранит первую переменную с нулем или андейайенд. она не задпна. поэтому вернет 2- значение:
//let car;
//console.log(car ?? 'fiat');
//
//let mess = "HI GUYS!";
//num = 5;
//if (5 > 3) console.log(mess);
//if (num > 10){
//    console.log(mess);
//}else {
//    console.log("no nono");
//}
//
//let messend = (2>1)  ? ", Carl" : ", John";
//mess += messend;
//console.log(mess);
//
//while (num <= 10) {
//    console.log(num);
//    num++;
//    }
//
//
////for
//for (let i=0; i<7; i++)  {
//    console.log(i);
//}
//
//
//let numb = 0;
//for(; numb<5; numb++) {
//    console.log(numb);
//    if (numb == 2) break;
//}
//console.log(`number is: ${numb}`);
//
////CONTINUE cintinue
//let numbc = 0;
//for(; numbc<5; numbc++) {
//
//    if (numbc == 2) continue;
//    console.log(`numr is: ${numbc}`);
//}
////console.log(`number is: ${numb}`);
////function
//
//function showClient(){
//    console.log('client');
//    }
//
//showClient();
//
//
////recursion
//
//function calcSumm(numOne, numTwo){
//    let result = 1;
//    for (let i=0; i < numTwo; i++) {
//        result *=
//    }
//    }
//
//let stavkaForKotirivka ={
//    perevozchik: {
//        perevozchik_name: "ООО Сдэк",
//        perevozchik_price: "200 byn",
//    },
//    komentariy: "some comment",
//}
//
//console.log(stavkaForKotirivka);
//console.log(stavkaForKotirivka.perevozchik);
//
//
//
//function makeStavka(perev_name, perevozchik_price, comment) {
//        return {
//            perev_name: perev_name,
//            perevozchik_price: perevozchik_price,
//            comment: comment,
//        };
//    }
//
//
//let stavka1 = makeStavka("ООО СДЭК", "258 EUR", "ЭТО СДЕЛКА ДЛЯ ЭТАПА ПУТИ ДО СМОРГОНИ");
//console.log(stavka1);
//stavka1.question = "que pasa?";
//console.log(stavka1);
//delete stavka1.question;
//console.log(stavka1);
//
//
//if ("nn" in stavka1){
//console.log(stavka1.nn);
//}else{
//console.log('no nn');}
//
//for (let key in stavka1){
//console.log(key);}
//
//function kotirova(stavka) {
//    this.stavka=stavka;
//}
//
//console.log(new kotirova(stavka1));
//console.log(Math.round(2.55));
//
////isFinite  isNaN
//console.log(isNaN("ji"+3));
//console.log(isFinite(3.5));
//
////massives
//
//let arrOne = [
//    'vanys',
//    'Liuba',
//    'petya',
//    function(){
//    console.log('why undefined?');}
//];
//console.log(arrOne[1]);
//console.log(arrOne[3]());
//console.log(typeof(arrOne[3]));
//console.log(typeof(arrOne[1]));
//
//let matrix = [
//[1, 3, 5],
//[2, 4, 6],
//]
//
//console.log(matrix[0][1]);
//console.log(matrix.length);
//matrix[2] = [7, 9, 9];
//console.log(matrix);
//
//
//matrix.push('el'); //adding element to the end of array
//console.log(matrix);
//
//matrix.shift();//deleting the first el of array
//console.log(matrix);
//
//matrix.pop(); //deleting the last el of array
//console.log(matrix);
//
//matrix.unshift([1, 3, 5],);   // edding el(-s) to the begining of array
//console.log(matrix);
//
////копирование массива slice, concat
////indexof includes    find findIndex filter
////sort reverse
////map
////split, join
//
//for (let i=0; i < matrix.length; i++) {
//    console.log("this is  - "+ matrix[i]);
//}
//
//
////forEach
//matrix.forEach(function (item, index, array) {
//    console.log("this is  - " + matrix[item] + ", index " + matrix[index]);
//});


//reduce

//////   DOM!!!!
//console.log(navigator.userAgent);
//console.log(location.href);

//history.back();

//alert confirm prompt
//console.log(prompt("who is sexylady?"));

//const htmlEl = document.documentElement;
//const hOne = htmlEl.H1;
//
//const headEl = document.head;

//const bodyEl = document.body;
//const firstCh = bodyEl.firstChild;

//console.log(firstCh);
//console.log(hOne);

const elClass = document.querySelectorAll('.block');
console.log(elClass);


const elClassli = document.querySelectorAll('li');
console.log(elClassli);
//for (const item of elems) {
//    console.log(item);
//}

//
//const elClassid = document.querySelectorAll('#hh');
//console.log(elClassid);
//
//const elid = document.getElementById('hh');
//console.log(elid);
//
//const button = document.getElementById("button");
//button.onclick = () => alert("you clicked me");
//






