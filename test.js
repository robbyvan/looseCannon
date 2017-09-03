function Test() {
  this.nums = [];
  this.pos = {};
}

Test.prototype = {
  insert: function(val) {
    this.nums.push(val);
    this.pos[val] = this.nums.length - 1;
  },
  remove: function(val) {
    this.nums = this.nums.filter(function(item) {
      return item !== val
    });
  },
};

var a = new Test();
a.insert(1);
a.insert(2);
a.insert(3);
a.remove(2);