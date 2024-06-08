// // Сложить два числа
// let a,b,c;
// a=-10;
// b=15;
// c=a+b;
// // Вернуть наиболшее из 3х числел
// console.log("Сложить два числа - ",c);
// if ((a>b) && (a>c)) {
//     console.log("Вернуть наиболшее из 3х числел - ",a)
// } else 
// if ((b>a) && (b>c)) {
//     console.log("Вернуть наиболшее из 3х числел - ",b)
// } else 
// if ((c>b) && (c>a)) {
//     console.log("Вернуть наиболшее из 3х числел - ",c)
// } 
// // Вернуть самую длинную строку
// let Text_1="топот";
// let Text_2="мышь";
// let Text_3="абажур";
// if ((Text_1.length>Text_2.length) && (Text_1.length>Text_3.length)) {
//     console.log("Вернуть самую длинную строку - ",Text_1)
// } else 
// if ((Text_2.length>Text_1.length) && (Text_2.length>Text_3.length)) {
//     console.log("Вернуть самую длинную строку - ",Text_2)
// } else 
// if ((Text_3.length>Text_1.length) && (Text_3.length>Text_2.length)) {
//     console.log("Вернуть самую длинную строку - ",Text_3)
// } 
// //Является ли слово палиндромом?
// function palindrom(Text_n){
//     let n = Text_n.length-1;
//     let palin = 0;
//     for ( let i = 0; i < n/2; i++)  {
//         if (Text_n[i]==Text_n[n-i]) {
//             palin = 1;
//         }
//         else {
//             palin = 0;
//             break;
//         }
//     }
//     if (palin)
//     console.log(Text_n," - слово палиндром"); else
//     console.log(Text_n," - слово не палиндром");
// }
// palindrom(Text_1);
// palindrom(Text_2);
// palindrom(Text_3);
// //сумма элементов массива
// let massiv = [5,2,1,3,4];
// let result = massiv.reduce((sum, current) => sum + current, 0);
// console.log("сумма элементов массива - ",result);
// //сортировка
// for (let j = massiv.length - 1; j > 0; j--) {
//     for (let i = 0; i < j; i++) {
//     if (massiv[i] > massiv[i + 1]) {
//         let temp = massiv[i];
//         massiv[i] = massiv[i + 1];
//         massiv[i + 1] = temp;
//     }
//     }
// }
//   console.log("Отфильтровать массив чисел -",massiv);
// //массив объектов 
// let object = [{ name: "Bob", age: 50}, { name: "Jane", age: 64}, { name: "Jack", age: 25}];
// let done = object.filter(index => index.age <= 50);
// console.log("Отфильтровать массив объектов - ",done);
// //склонировать объект
// let object_2 = { name: "Bob", age: 50, children: [ { name: "Marie", age: 16}, { name: "Jame", age: 12} ] };
// let clone = {}
// let child = object_2.children;
// for (let key in object_2) {
//     if (key == 'children') 
//         clone.children=object_2.children.slice();
//     else
//     clone[key] = object_2[key];
// }
// console.log("Склонировать объект  - ",clone);
// // const clone3 = structuredClone(object_2);
// // const clone2 = JSON.parse('obj-from-backend');
// import (api-response.json)
