$(document).ready(function () {
    let forms = $('.follow-unfollow-form');
    forms.each((index, el) => {
        $(el).on('submit', (e) => {
            e.preventDefault();
            $.ajax({
                type: $(el).attr('method'),
                url: $(el).attr('action'),
                data: $(el).serialize(),
                success: function (response) {
                    if (response['succeed']) {
                        if ($(el).hasClass('unfollow-form')) {
                            $(el).removeClass('unfollow-form').addClass('follow-form');
                            $(el).attr('action', '/follow/');

                            $(el).find('.follow-btn-wrap').empty();
                            $(el).find('.follow-btn-wrap').html(`
                                <button type="submit" class="btn-sm btn-outline-danger text-gray">Подписаться</button>
                            `);
                        } else if ($(el).hasClass('follow-form')) {
                            $(el).removeClass('follow-form').addClass('unfollow-form');
                            $(el).attr('action', '/unfollow/');

                            $(el).find('.follow-btn-wrap').empty();
                            $(el).find('.follow-btn-wrap').html(`
                                <button type="submit" class="btn-sm btn-outline-danger active">Отписаться</button>
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