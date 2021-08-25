
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