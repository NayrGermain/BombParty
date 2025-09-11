const app = require("./app.js");
const port = process.env.PORT;

//Activation du port
app.listen(port, () => {
    console.log(`Serveur actif sur le port ${port}`);
});