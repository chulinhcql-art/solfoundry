const express = require('express');
const http = require('http');
const socketIo = require('socket.io');

class NotificationService {
    constructor(server) {
        this.io = socketIo(server, {
            cors: { origin: "*" }
        });
        this.setupListeners();
    }

    setupListeners() {
        this.io.on('connection', (socket) => {
            print(`[v10.6] Client connected: ${socket.id}`);
            
            socket.on('subscribe_to_events', (data) => {
                socket.join(data.walletAddress);
                print(`[v10.6] Wallet ${data.walletAddress} subscribed.`);
            });
        });
    }

    sendNotification(walletAddress, message) {
        this.io.to(walletAddress).emit('notification', {
            title: 'SolFoundry Alert',
            body: message,
            timestamp: new Date()
        });
    }
}

module.exports = NotificationService;
