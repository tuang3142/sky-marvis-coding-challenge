## Problem

Design a Google Translate application.

## Approach

To translate a sentence, first, we break down the sentence into words, then do the translation word by word. So the problem can be boiled down to:
- translate between English and other languages.
- translate between non-English languages.

First, translating English words into other languages is simple. Cambridge dictionary is a well-known and reliable source. They have an available [API](https://dictionary-api.cambridge.org/) to translate up to 12 languages into English. We would use this as the database for the application.

We will store these dictionaries as separates database tables which are hash-maps with the English word as the key and the translation as value. For example, assuming we are translating from English to Vietnamese, we would have the following database:

```
english_to_vietnamese_dict = {
  apple: táo
  ball: bóng
  chicken: gà
  ...
}
```

This would help the translation time to be near-instant as we would simply retrieve the translation value from the hash table. We would also have the dictionary duplicated to translate from Vietnamese to English:

```
vietnamese_to_english_dict = {
  táo: apple
  bóng: ball
  gà: chicken
  ...
}
```

This would double the storage needed in exchange for the instant translation time.

After the first problem is resolved, the second problem should be easy by utilizing the above database. For example, assuming we are translating from Chinese to Vietnamese, first we translate Chinese to English, translate from English to Vietnamese.

The flow of the application can be summed up as below:

[![](https://mermaid.ink/img/eyJjb2RlIjoiZ3JhcGggVERcbiAgICBBW1RyYW5zbGF0ZSBhIHNlbnRlbmNlIGZyb20gQ2hpbmVzZSB0byBWaWV0bmFtZXNlXSBcbiAgICAtLT5CW0JyZWFrIGRvd24gc2VudGVuZXNlIHRvIHdvcmRzXVxuICAgIC0tPkNbTG9vayB1cCBFbmdpc2ggdHJhbnNsYXRpb24gZm9yIGVhY2ggd29yZF1cbiAgICBLW0pvaW4gdGhlIHdvcmRzLCB0aGVuIHJldHVybiB0aGUgc2VudGVuY2VdXG4gICAgQyAtLT58Q2hpbmVzZSBXb3JkfCBEW3RvIEVuZ2xpc2hdIC0tPiBHW3RvIFZpZXRuYW1lc2VdIC0tPiBLIFxuICAgIEMgLS0-fENoaW5lc2UgV29yZHwgRVt0byBFbmdsaXNoXSAtLT4gSFt0byBWaWV0bmFtZXNlXSAtLT4gS1xuICAgIEMgLS0-fENoaW5lc2UgV29yZHwgRlt0byBFbmdsaXNoXSAtLT4gSVt0byBWaWV0bmFtZXNlXSAtLT4gSyIsIm1lcm1haWQiOnsidGhlbWUiOiJkZWZhdWx0In0sInVwZGF0ZUVkaXRvciI6ZmFsc2UsImF1dG9TeW5jIjp0cnVlLCJ1cGRhdGVEaWFncmFtIjpmYWxzZX0)](https://mermaid-js.github.io/mermaid-live-editor/edit##eyJjb2RlIjoiZ3JhcGggVERcbiAgICBBW1RyYW5zbGF0ZSBhIHNlbnRlbmNlIGZyb20gQ2hpbmVzZSB0byBWaWV0bmFtZXNlXSBcbiAgICAtLT5CW0JyZWFrIGRvd24gc2VudGVuZXNlIHRvIHdvcmRzXVxuICAgIC0tPkNbTG9vayB1cCBFbmdpc2ggdHJhbnNsYXRpb24gZm9yIGVhY2ggd29yZF1cbiAgICBLW29pbiB0aGUgd29yZHMsIHRoZW4gcmV0dXJuIHRoZSBzZW50ZW5jZV1cbiAgICBDIC0tPnxDaGluZXNlIFdvcmR8IERbdG8gRW5nbGlzaF0gLS0-IEdbdG8gVmlldG5hbWVzZV0gLS0-IEsgXG4gICAgQyAtLT58Q2hpbmVzZSBXb3JkfCBFW3RvIEVuZ2xpc2hdIC0tPiBIW3RvIFZpZXRuYW1lc2VdIC0tPiBLXG4gICAgQyAtLT58Q2hpbmVzZSBXb3JkfCBGW3RvIEVuZ2xpc2hdIC0tPiBJW3RvIFZpZXRuYW1lc2VdIC0tPiBLIiwibWVybWFpZCI6IntcbiAgXCJ0aGVtZVwiOiBcImRlZmF1bHRcIlxufSIsInVwZGF0ZUVkaXRvciI6ZmFsc2UsImF1dG9TeW5jIjp0cnVlLCJ1cGRhdGVEaWFncmFtIjpmYWxzZX0)
