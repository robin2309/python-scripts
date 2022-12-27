const http = require("http");

const server = http.createServer((req, res) => {
  if (req.method === "POST") {
    // Respond with a 200 status code
    res.writeHead(200);
    res.end();
  } else {
    // Respond with a 405 status code for other methods
    res.writeHead(405);
    res.end();
  }
});

server.listen(3000, () => {
  console.log("Server listening on port 3000");
});
