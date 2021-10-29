
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

// -------- To Be Continued -------
// -------- Currency Converter API Fetch -----
const fromCurrency = document.querySelector('.from-form-select');
const toCurrency = document.querySelector('.to-form-select');

// Get selected Value

fromCurrency.addEventListener('change', (e) => {
  console.log(e.target.value)
})

const getCurrencyData = () => {
  const currencyArray = []
  console.log(currencyArray)

  url = "https://free.currconv.com/api/v7/countries?apiKey=da439e3f05f695b038df"
  fetch(url)
  .then(response => response.json())
  .then(data => {
    for (const [key, value] of Object.entries(data['results'])){
      var currencyId = value['currencyId']
      var currencyName = value['currencyName']
      var currObj = {
        'currencyID': currencyId,
        'currencyName': currencyName
      }
      currencyArray.push(currObj)
    }
  })
  console.log(currencyArray)
}

getCurrencyData()

const convertCurrency = () => {
  var _from = document.querySelector('.amount-from-form_number')
  var to = document.querySelector('.amount-from-form_curr')
  convert_url = "https://free.currconv.com/api/v7/convert?q="+_from+"_"+to+"&compact=ultra&apiKey="+API_KEY
}










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
