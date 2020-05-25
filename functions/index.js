const functions = require("firebase-functions");
const express = require("express");
const bodyParser = require("body-parser");

// // Create and Deploy Your First Cloud Functions
// // https://firebase.google.com/docs/functions/write-firebase-functions
//
const app = express();

app.use(bodyParser.json());

app.get("/getAppProperties", (req, res) => {
  res.statusCode = 200;
  res.setHeader("Content-Type", "application/json");
  res.setHeader("Access-Control-Allow-Origin", "*");
  res.json({
    title: "Learn",
    allModules: {
      text: "All Modules",
      url: "/modules",
      scheme: "/modules",
    },
  });
});

app.get("/modules/list", (req, res) => {
  res.setHeader("Access-Control-Allow-Origin", "*");
  const listData = {
    title: "Modules",
    modules: {
      baseUrl: "/modules",
      list: [
        { text: "Python", url: "/python", scheme: "/[moduleId]" },
        { text: "SQL", url: "/sql", scheme: "/[moduleId]" },
        { text: "Math", url: "/math", scheme: "/[moduleId]" },
        { text: "Statistics", url: "/statistics", scheme: "/[moduleId]" },
        { text: "AI & ML 1", url: "/ai-ml-1", scheme: "/[moduleId]" },
        { text: "AI & ML 2", url: "/ai-ml-2", scheme: "/[moduleId]" },
        {
          text: "Linear Regression",
          url: "/linear-regression",
          scheme: "/[moduleId]",
        },
        {
          text: "Simple Linear Regression",
          url: "/simple-linear-regression",
          scheme: "/[moduleId]",
        },
      ],
    },
  };

  const { top } = req.query;
  const listDataTop5 = {
    title: "Modules",
    modules: {
      baseUrl: "/modules",
      list: [
        { text: "Python", url: "/python", scheme: "/[moduleId]" },
        { text: "AI & ML 1", url: "/ai-ml-1", scheme: "/[moduleId]" },
        { text: "AI & ML 2", url: "/ai-ml-2", scheme: "/[moduleId]" },
        {
          text: "Linear Regression",
          url: "/linear-regression",
          scheme: "/[moduleId]",
        },
        {
          text: "Simple Linear Regression",
          url: "/simple-linear-regression",
          scheme: "/[moduleId]",
        },
      ],
    },
  };

  return top ? res.json(listDataTop5) : res.json(listData);
});

const getModuleName = (id) => {
  switch (id.toLowerCase()) {
    case "python":
      return { text: "Python", title: "Python Learning Modules" };
    case "sql":
      return { text: "SQL", title: "SQL Learning Modules" };
    case "math":
      return { text: "Mathematics", title: "Mathematics Learning Modules" };
    case "statistics":
      return { text: "Statistics", title: "Statistics Learning Modules" };
    case "ai-ml-1":
      return {
        text: "Artificial & Maching Learning (I)",
        title: "Artificial & Maching Learning (I) Learning Modules",
      };
    case "ai-ml-2":
      return {
        text: "Artificial & Maching Learning (II)",
        title: "Artificial & Maching Learning (II) Learning Modules",
      };
    case "linear-regression":
      return {
        text: "Linear Regression",
        title: "Linear Regression Learning Modules",
      };
    case "simple-linear-regression":
      return {
        text: "Simple Linear Regression",
        title: "Simple Linear Regression Learning Modules",
      };
    default:
      return { text: id, title: "Unknown Module" };
  }
};

app.get("/modules/:moduleId", (req, res) => {
  res.setHeader("Access-Control-Allow-Origin", "*");
  const data = getModuleName(req.params.moduleId);
  return res.json({
    title: data.title,
    modules: {
      text: data.text,
      url: `/${req.params.moduleId}`,
      scheme: "/[moduleId]",
    },
  });
});

exports.api = functions.https.onRequest(app);
