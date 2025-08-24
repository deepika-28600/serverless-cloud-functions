/**
 * HTTP Cloud Function.
 * POST { "url": "https://..." } -> { code }
 * GET  ?code=xxxxxxx -> 302 redirect
 */
exports.shortener = (req, res) => {
  if (req.method === 'POST') {
    const url = req.body && req.body.url;
    if (!url) return res.status(400).json({ error: 'url required' });
    const code = require('crypto').createHash('md5').update(url).digest('hex').slice(0,7);
    // TODO: save to Firestore
    return res.status(201).json({ code, url });
  } else {
    const code = req.query.code;
    if (!code) return res.status(400).json({ error: 'code required' });
    // TODO: fetch from Firestore and redirect
    return res.redirect(302, 'https://example.com');
  }
};
