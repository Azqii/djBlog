$(document).ready(function() {
    let forms = $('.like-unlike-form');
    forms.each((index, el) => {
        $(el).on('submit', (e) => {
            e.preventDefault();
            $.ajax({
                type: $(el).attr('method'),
                url: $(el).attr('action'),
                data: $(el).serialize(),
                success: function (response) {
                    if (response['succeed']) {
                        if ($(el).hasClass('like-form')) {
                            $(el).removeClass('like-form').addClass('unlike-form');
                            $(el).attr('action', '/post/unlike/');

                            $(el).find('.button-wrap').empty();
                            $(el).find('.button-wrap').html(`
                                <button type="submit" class="btn btn-outline-danger active">
                                    <i class="fa fa-thumbs-up like-button"> ${response['likes']}</i>
                                </button>
                            `);
                        }
                        else if ($(el).hasClass('unlike-form')) {
                            $(el).removeClass('unlike-form').addClass('like-form');
                            $(el).attr('action', '/post/like/');

                            $(el).find('.button-wrap').empty();
                            $(el).find('.button-wrap').html(`
                                <button type="submit" class="btn btn-outline-danger">
                                    <i class="fa fa-thumbs-up like-button"> ${response['likes']}</i>
                                </button>
                            `);
                        }
                    }
                    else {
                        alert("Что-то пошло не так");
                    }
                }
            })
        })
    })
})
