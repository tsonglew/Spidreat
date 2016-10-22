var superagent = require('superagent');
var cheerio = require('cheerio');

superagent
.get('https://segmentfault.com/t/python/blogs')
.end(function(err, res) {
    console.log('\nSegmentFault Python...\n');
    var $ = cheerio.load(res.text);
    $('h2[class=title]').each(function(i, elem) {
        console.log({
            'title': $(this).text(),
            'href': 'https://segmentfault.com' + $(this).find('a').attr('href')
            });
    });
});

superagent
.get('https://segmentfault.com/t/javascript/blogs')
.end(function(err, res) {
    console.log('\nSegmentFault JavaScript...\n');
    var $ = cheerio.load(res.text);
    $('h2[class=title]').each(function(i, elem) {
        console.log({
            'title': $(this).text(),
            'href': 'https://segmentfault.com' + $(this).find('a').attr('href')
        });
    });
});

superagent
.get('https://segmentfault.com/t/node.js/blogs')
.end(function(err, res) {
    console.log('\nSegmentFault Node.js...\n');
    var $ = cheerio.load(res.text);
    $('h2[class=title]').each(function(i, elem) {
        console.log({
            'title': $(this).text(),
            'href': 'https://segmentfault.com' + $(this).find('a').attr('href')
        });
    });
});

superagent
.get('https://segmentfault.com/t/android/blogs')
.end(function(err, res) {
    console.log('\nSegmentFault Android...\n');
    var $ = cheerio.load(res.text);
    $('h2[class=title]').each(function(i, elem) {
        console.log({
            'title': $(this).text(),
            'href': 'https://segmentfault.com' + $(this).find('a').attr('href')
        });
    });
});
