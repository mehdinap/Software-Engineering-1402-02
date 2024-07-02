// static/chat/js/chat.js
$(document).ready(function () {
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    const csrftoken = getCookie('csrftoken');

    $.ajaxSetup({
        beforeSend: function (xhr, settings) {
            if (!/^(GET|HEAD|OPTIONS|TRACE)$/.test(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

    // Function to load FAQ roots
    function loadFAQs(faqId = null) {
        $.ajax({
            url: faqId ? `/group6/faq/${faqId}/children/` : '/group6/faq/roots/',
            method: 'GET',
            success: function (data) {
                $('#faq-list').empty();
                data.forEach(function (item) {
                    $('#faq-list').append(`<li data-id="${item.id}">${item.text}</li>`);
                });
            }
        });
    }

    // Load FAQs on page load
    loadFAQs();

    // Fetch FAQ children on click
    $(document).on('click', '#faq-list li', function () {
        const faqId = $(this).data('id');
        loadFAQs(faqId);
    });

    let currentChatId = null;
    let currentUser = $('#user-id').val();  // Assuming you set user id in a hidden field or similar

    // Function to load chat messages
    function loadMessages(chatId) {
        $.ajax({
            url: `/group6/get-messages/${chatId}/`,
            method: 'GET',
            success: function (data) {
                $('#messages').empty();
                data.forEach(function (message) {
                    let messageClass = message.sender == currentUser ? 'me' : 'support';
                    $('#messages').append(`<div class="message ${messageClass}">${message.text}</div>`);
                    $('#messages').scrollTop($('#messages')[0].scrollHeight);
                });
            }
        });
    }

    // Function to send message
    function sendMessage(chatId, text) {
        $.ajax({
            url: `/group6/send-message/`,
            method: 'POST',
            data: {
                text: text,
                chat_id: chatId
            },
            success: function (message) {
                loadMessages(chatId);
                $('#message-input').val('');
            }
        });
    }

    // Send message on button click
    $('#send-button').on('click', function () {
        let text = $('#message-input').val();
        if (text.trim() != '') {
            sendMessage(currentChatId, text);
        }
    });

    // Send message on Enter key press
    $('#message-input').on('keypress', function (e) {
        if (e.which == 13) {
            let text = $('#message-input').val();
            if (text.trim() != '') {
                sendMessage(currentChatId, text);
            }
        }
    });

    // Load messages periodically
    setInterval(function () {
        if (currentChatId) {
            loadMessages(currentChatId);
        }
    }, 3000);

    // Start a chat with support
    $('#start-chat').on('click', function () {
        $.ajax({
            url: '/group6/create-chat/',
            method: 'POST',
            success: function (data) {
                currentChatId = data.id;
                loadMessages(currentChatId);
            }
        });
    });

    // Set chat id
    $('#input-chat-id').on('change', function () {
        currentChatId = document.querySelector("#input-chat-id").value;
        loadMessages(currentChatId);
    });
});
