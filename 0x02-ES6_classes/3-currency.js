export default class Currency {
  constructor(code, name) {
    this.code = code;
    this.name = name;
  }

  get name() { return this._name; }

  set name(value) {
    if (typeof (value) !== 'string') { throw TypeError('Name must be a string'); }
    this._name = value;
  }

  get code() { return this._code; }

  set code(value) {
    if (typeof (value) !== 'string') { throw TypeError('code must be a string containing a symbol'); }
    this._code = value;
  }

  displayFullCurrency() {
    return `${this._name} (${this._code})`;
  }
}
