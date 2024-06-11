const spawner = require("child_process").spawn;
const { Router } = require("express");

const api = Router();

api.get("", (req, res) => {
  const python_process = spawner("python", ["./index.py"]);

  console.log("first");

  python_process.stdout.on("data", (data) => {
    res.render("index", {
      ref_cols: JSON.parse(data),
    });
  });

  python_process.stderr.on("data", (err) => {
    console.log(err.toString());
  });
});

api.post("", async (req, res, next) => {
  cols = req.body;

  const python_process = spawner("python", [
    "./model.py",
    JSON.stringify(cols),
  ]);

  python_process.stdout.on("data", async (data) => {
    let results = await JSON.parse(data);
    console.log(results);
    res.json(Math.round(results));
    next();
  });


});

module.exports = api;
