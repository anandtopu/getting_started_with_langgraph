/** Block networking in Node grading children; installation is a separate explicit step. */
import net from "node:net";
import tls from "node:tls";
import http from "node:http";
import https from "node:https";
import dns from "node:dns";
function blocked() { throw new Error("Offline TypeScript exercise attempted network access"); }
net.Socket.prototype.connect = blocked;
tls.connect = blocked;
http.request = http.get = https.request = https.get = blocked;
dns.lookup = dns.resolve = blocked;
globalThis.fetch = blocked;
