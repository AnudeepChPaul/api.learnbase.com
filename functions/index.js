const functions = require("firebase-functions");
const express = require("express");

// // Create and Deploy Your First Cloud Functions
// // https://firebase.google.com/docs/functions/write-firebase-functions
//

const app = express();

app.get("/getAppProperties", (req, res) => {
  res.statusCode = 200;
  res.setHeader("Content-Type", "application/json");
  res.json({
    title: "Create Next App",
    header: {
      title: "Home",
      url: "/",
      modules: {
        text: "All Modules",
        url: "/modules",
        scheme: "/modules",
        list: [
          { text: "Python", url: "/python", scheme: "/[moduleId]" },
          { text: "SQL", url: "/sql", scheme: "/[moduleId]" },
          { text: "Math", url: "/math", scheme: "/[moduleId]" },
          { text: "Statistics", url: "/statistics", scheme: "/[moduleId]" },
          { text: "AI & ML 1", url: "/ai-ml-1", scheme: "/[moduleId]" },
        ],
      },
      buttons: [{ text: "About", url: "/about", scheme: "/about" }],
    },
  });
});


app.get('/modules', (req,res) => {
  return res.json({
    title: 'Modules'
    , modules: {
      text: 'All Modules'
      , url: '/modules'
      , scheme: '/modules'
      , list: [
        { text: "Python", url: "/python", scheme: '/[moduleId]' },
        { text: "SQL", url: "/sql", scheme: '/[moduleId]' },
        { text: "Math", url: "/math" , scheme: '/[moduleId]'},
        { text: "Statistics", url: "/statistics", scheme: '/[moduleId]' },
        { text: "AI & ML 1", url: "/ai-ml-1", scheme: '/[moduleId]' }
      ]
    }
  })
})

app.get('/modules/:moduleId', (req,res) => {
  return res.json({
    title: 'Modules'
    , modules: {
      text: 'Python'
      , url: '/python'
      , scheme: '/[moduleId]'
    }
  })
})

exports.api = functions.https.onRequest(app);
