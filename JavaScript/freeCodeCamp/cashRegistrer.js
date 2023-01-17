/*==========
freeCodeCamp last project - Cash Registrer.
Design a cash register drawer function checkCashRegister() that accepts purchase price as the first argument (price), payment as the second argument (cash), and cash-in-drawer (cid) as the third argument.

cid is a 2D array listing available currency.

The checkCashRegister() function should always return an object with a status key and a change key.

Return {status: "INSUFFICIENT_FUNDS", change: []} if cash-in-drawer is less than the change due, or if you cannot return the exact change.

Return {status: "CLOSED", change: [...]} with cash-in-drawer as the value for the key change if it is equal to the change due.

Otherwise, return {status: "OPEN", change: [...]}, with the change due in coins and bills, sorted in highest to lowest order, as the value of the change key.
==========*/


const checkCashRegister = (price, cash, cid) => {
  const UNIT_AMOUNT = {
      "PENNY": .01,
      "NICKEL": .05,
      "DIME": .10,
      "QUARTER": .25,
      "ONE": 1.00,
      "FIVE": 5.00,
      "TEN": 10.00,
      "TWENTY": 20.00,
      "ONE HUNDRED": 100.00
  }

  let sum = 0;
  let change = cash - price;
  const result = [];
  for (let i = 0; i < cid.length; i++) {
      sum += cid[i][1];
  }
  sum = sum.toFixed(2);
  if (change > sum) {
      return {status: 'INSUFFICIENT_FUNDS', change: result};
  } else if (change.toFixed(2) === sum){
      return {status: "CLOSED", change: cid};
  } else {
      cid = cid.reverse();
      for (let i of cid) {
          let tmp = [i[0],0];
          while(change >= UNIT_AMOUNT[i[0]] && i[1] > 0) {
              tmp[1] += UNIT_AMOUNT[i[0]];
              i[1] -= UNIT_AMOUNT[i[0]];
              change -= UNIT_AMOUNT[i[0]];
              change = change.toFixed(2);
          }

          if (tmp[1] > 0) {
              result.push(tmp)
          }
       }
  }

  if (change > 0) {
      return {status: 'INSUFFICIENT_FUNDS', change: []}
  }

  return { status: 'OPEN', change: result};
}

console.log(checkCashRegister(19.5, 20, [["PENNY", 1.01], ["NICKEL", 2.05], ["DIME", 3.1], ["QUARTER", 4.25], ["ONE", 90], ["FIVE", 55], ["TEN", 20], ["TWENTY", 60], ["ONE HUNDRED", 100]]))
//Output: { status: 'OPEN', change: [ [ 'QUARTER', 0.5 ] ] }