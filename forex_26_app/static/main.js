
/* --------============== Navigation Bar ===========------- */
/* --- Applicable to the layout.html file ---- */

// --- ===== SHOW / HIDE NAVBAR ===== ---

const navBar = document.querySelector('.nav-bar');
const bxMenu = document.querySelector('.bx-menu');
const bxX = document.querySelector('.bx-x');

// --------- ===== ===-- Show NavBar --=== ===== -----------
bxMenu.addEventListener('click', () => {
  navBar.classList.toggle('show-navbar');
  bxMenu.classList.toggle('hide-icon');
  bxX.classList.toggle('show-icon');
})


// --------- ===== ===-- Hide NavBar --=== ===== -----------

bxX.addEventListener('click', () => {
  if(bxMenu.classList.contains('hide-icon') && navBar.classList.contains('show-navbar')) {
    bxMenu.classList.remove('hide-icon');
    navBar.classList.remove('show-navbar');
    bxX.classList.remove('show-icon');
  }
})

/* --------============== Signals ===========------- */
/* --- Applicable to the signals.html file ---- */

signalActions = document.querySelectorAll('.call-to-buy-txt');
signalArrows = document.querySelectorAll('.arrow-sell-buy');

/*
check if signal action is sell or buy then change
the background color and color
*/
signalActions.forEach(signalAction => {
  if((signalAction.textContent).toLowerCase() === 'sell'){
    signalAction.style.backgroundColor = "#ffd4d8"
    signalAction.style.color = "#d33b25"
  }else if ((signalAction.textContent).toLowerCase() === 'buy'){
    signalAction.style.backgroundColor = "#cfe2e0"
    signalAction.style.color = "#05697f"
  }
});

/*
check if signal action is sell or buy then change
the arrow directions
*/

signalArrows.forEach(signalArrow => {
  var signalParent = signalArrow.parentNode // Get signal arrow parent node
  var signalActionName = signalParent.previousElementSibling.textContent // then it's siblings to find inside if it's sell or buy

  if((signalActionName).toLowerCase() === 'sell'){
    signalArrow.classList.remove('bx-up-arrow-alt')
    signalArrow.classList.add('bx-down-arrow-alt')
  }else if ((signalActionName).toLowerCase() === 'buy'){
    signalArrow.classList.remove('bx-down-arrow-alt')
    signalArrow.classList.add('bx-up-arrow-alt')
  }
});

// -=========== Currency Converter =============-
// -- focus the amount input on mouseover and unfocus it on mouseleave --

// focus
const amountInput = document.querySelector('.amount-input')
amountInput.addEventListener('mouseover', () => {
  amountInput.focus()
})

// unfocus
amountInput.addEventListener('mouseleave', () => {
  amountInput.blur()
})

/*
get currencies and keep them localy
in order to show them when the browser refreshed
*/

const currConverterForm = document.querySelector('.curr-converter-form')
const selectInputFrom = document.querySelector('.from')
const selectInputTo = document.querySelector('.to')

/*
check in local storage recent currencies then populate them
*/
if(localStorage.getItem('convertAmount')) {
  amountInput.value = localStorage.getItem('convertAmount')
}
console.log
// --
selectInputFrom.options[ selectInputFrom.selectedIndex ].value = localStorage.getItem('from')
selectInputFrom.options[ selectInputFrom.selectedIndex ].textContent = localStorage.getItem('from_Name')
// to
selectInputTo.options[ selectInputTo.selectedIndex ].value = localStorage.getItem('to')
selectInputTo.options[ selectInputTo.selectedIndex ].textContent = localStorage.getItem('to_Name')
// ----------------------- 

currConverterForm.addEventListener('submit', (e) => {
  if(localStorage.getItem('convertAmount') && localStorage.getItem('from') && localStorage.getItem('to') && localStorage.getItem('from_Name') && localStorage.getItem('to_Name')) {
    localStorage.removeItem('convertAmount')
    // --
    localStorage.removeItem('from')
    localStorage.removeItem('from_Name')
    // to
    localStorage.removeItem('to')
    localStorage.removeItem('to_Name')
    // --
    localStorage.setItem('convertAmount', amountInput.value)
    // -- 
    localStorage.setItem('from', selectInputFrom.options[ selectInputFrom.selectedIndex ].value)
    localStorage.setItem('from_Name', selectInputFrom.options[ selectInputFrom.selectedIndex ].textContent)
    // to
    localStorage.setItem('to', selectInputTo.options[ selectInputTo.selectedIndex ].value)
    localStorage.setItem('to_Name', selectInputTo.options[ selectInputTo.selectedIndex ].textContent)
  }
  else {
    localStorage.setItem('convertAmount', amountInput.value)
    // --
    localStorage.setItem('from', selectInputFrom.options[ selectInputFrom.selectedIndex ].value)
    localStorage.setItem('from_Name', selectInputFrom.options[ selectInputFrom.selectedIndex ].textContent)
    // to
    localStorage.setItem('to', selectInputTo.options[ selectInputTo.selectedIndex ].value)
    localStorage.setItem('to_Name', selectInputTo.options[ selectInputTo.selectedIndex ].textContent)
  }
})




// //  ============ NOTIFY BUTTON ==============
// Notification.requestPermission();
 
// function notifyUser() {
//     if (!("Notification" in window)) {
//       alert("This browser does not support system notifications");
//     }
//     else if (Notification.permission === "granted") {
//       notify();
//     }
//     else if (Notification.permission !== 'denied') {
//       Notification.requestPermission(function (permission) {
//         if (permission === "granted") {
//             showWelcomeNotification();
//         }
//       });
//     }
    
//     function notify() {
//       var notification = new Notification('NEW SIGNAL', {
//         icon: 'https://raw.githubusercontent.com/r-e-d-ant/Body-Mass-Index/master/link_overview_fav.jpg',
//         body: "Check there is a new signal!",
//       });
   
//       notification.onclick = function () {
//         window.open("https://www.forexleo24.com/signals");      
//       };
//       setTimeout(notification.close.bind(notification), 7000); 
//     }

//     function showWelcomeNotification() {
//       var notification = new Notification('NOTIFICATION ALLOWED', {
//         icon: 'https://raw.githubusercontent.com/r-e-d-ant/Body-Mass-Index/master/link_overview_fav.jpg',
//         body: "You will get notification on any new signal !",
//       });
   
//       notification.onclick = function () {
//         window.open("https://www.forexleo24.com/signals");      
//       };
//       setTimeout(notification.close.bind(notification), 7000); 
//     }
//   }
