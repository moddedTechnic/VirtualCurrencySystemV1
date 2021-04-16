module.exports = {
	env: {
		browser: true,
		commonjs: true,
		es2021: true,
	},
	extends: ['google'],
	parserOptions: {
		ecmaVersion: 12,
	},
	rules: {
		'quotes': ['warn', 'single'],
		'indent': ['error', 'tab'],
		'no-tabs': 0,
		'max-len': [
			'warn',
			{
				code: 90,
				tabWidth: 4,
				ignoreComments: true,
				ignoreTrailingComments: true,
				ignoreUrls: true,
				ignoreStrings: true,
				ignoreTemplateLiterals: true,
				ignoreRegExpLiterals: true,
			},
		],
		'linebreak-style': 'off',
	},
};
