const app = require("./app.js");
const PORT = process.env.PORT || 10000;

//Activation du port
app.listen(PORT, () => {
    console.log(`Serveur actif sur le port ${port}`);
});