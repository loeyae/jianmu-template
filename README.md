# jianmu-template

![GitHub package.json version](https://img.shields.io/github/package-json/v/frederick-wang/jianmu-template) ![GitHub language count](https://img.shields.io/github/languages/count/frederick-wang/jianmu-template) ![GitHub top language](https://img.shields.io/github/languages/top/frederick-wang/jianmu-template) ![GitHub](https://img.shields.io/github/license/frederick-wang/jianmu-template) ![last-commit](https://img.shields.io/github/last-commit/frederick-wang/jianmu-template) ![commit-activity](https://img.shields.io/github/commit-activity/m/frederick-wang/jianmu-template)

The project template of Jianmu Framework.

当出现以下错误
```shell
[tsc] ../../../../electron-log/src/index.d.ts(9,30): error TS7031: Binding element 'LogMessage' implicitly has an 'any' type.
Could not start Electron because of the above typescript error(s).   
```
修改`node_modules/electron-log/src/index.d.ts`第9行，添加@ts-ignore
```shell
  // @ts-ignore
  type Format = (({ message: LogMessage }) => any[]) | string;
```
