var transport = nodemailer.createTransport({
  host: "live.smtp.mailtrap.io",
  port: 587,
  auth: {
    user: "api",
    pass: "9f41bf210f677a1cdebc60fd8712982e"
  }
});

async function main() {
  const info = await transport.sendMail({
    from: '"Prueba" <maddison53@ethereal.email>', 
    to: "piedrapapeltijeragane@gmail.com",
    subject: "Hello ✔", 
    text: "Hello world?", 
    html: "<b>Hello world?</b>", 
  });

  console.log("Message sent: %s", info.messageId);
}

main().catch(console.error);