module.exports = {
  env: {
    browser: true,
    es2021: true,
  },
  extends: [
    'plugin:react/recommended',
    'airbnb'
  ],
  parserOptions: {
    ecmaFeatures: {
      jsx: true,
    },
    ecmaVersion: 12,
    sourceType: 'module',
  },
  plugins: [
    'react',
  ],
  rules: {
    "indent" : ["error", 4, { "ignoredNodes": ["JSXElement *"] }],
    "react/jsx-indent" : ["error", 4],
    "react/jsx-indent-props" : ["error", 4],
    "import/no-extraneous-dependencies": ["error", {"devDependencies": true}],
  },
  parser: "babel-eslint",
};
