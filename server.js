const express = require('express');
const nodemailer = require('nodemailer');
const bodyParser = require('body-parser');
const fs = require('fs');

const app = express();
const PORT = process.env.PORT || 3000;

app.use(bodyParser.json());

const transporter = nodemailer.createTransport({
    service: 'Gmail',
    auth: {
        user: 'socialspeed.contacto@gmail.com',
        pass: 's4aU9RzyD8HsT7RKyk2Hd' 
    }
});

app.post('/suscribirse', (req, res) => {
    const email = req.body.email;

    fs.readFile('C:/Users/marco/a-simple-responsive-html-email/legacy/HTML/index.html', 'utf8', (error, data) => {
        if (error) {
            console.log(error);
            res.status(500).send('Error al leer el archivo HTML');
            return;
        }

        const mailOptions = {
            from: 'socialspeed.contacto@gmail.com',
            to: email,
            subject: 'NewsLetter',
            html: data
        };

        transporter.sendMail(mailOptions, (error, info) => {
            if (error) {
                console.log(error);
                res.status(500).send('Error al enviar el correo electrónico');
            } else {
                console.log('Correo electrónico enviado: ' + info.response);
                res.status(200).send('Correo electrónico enviado con éxito');
            }
        });
    });
});

app.listen(PORT, () => {
    console.log(`Servidor en ejecución en el puerto ${PORT}`);
});