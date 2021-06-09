$(document).ready(function () {
});

$("#LoginBtn").bind("click", function () {
    const form = document.forms["Login"];
    const Account = form.elements.Account.value;
    const Password = form.elements.Password.value;
    var data = {
        Account: Account,
        Password: Password
    }
    $.ajax({
        url: '/_login',
        type: 'GET',
        data: data,
        beforeSend: function () {
        },
        success: function (result) {
            if (result['Passed'])
                window.location = '/home';
            else
                alert("login failed")
        },
        complete: function () {
        },
        error: function () {
        }
    })
})

$("#RegisterBtn").bind("click", function () {
    const form = document.forms["Register"];
    const Account = form.elements.Account.value;
    const Password = form.elements.Password.value;
    const ConfirmPassword = form.elements.ConfirmPassword.value;
    const PhoneNumber = form.elements.PhoneNumber.value;
    var data = {
        Account: Account,
        Password: Password,
        ConfirmPassword: ConfirmPassword,
        PhoneNumber: PhoneNumber
    }
    errHead = '<nobr id="errMsg">';
    errEnd = '</nobr>';
    $.ajax({
        url: '/_register',
        type: 'GET',
        data: data,
        beforeSend: function () {
            $("nobr").remove('#errMsg');
        },
        success: function (result) {
            if (result[0] == 'Register success!') {
                alert(result[0]);
                window.location = '/';
            }
            else {
                if (result[0] != '')
                    $('#M0').append(errHead + result[0] + errEnd)
                if (result[1] != '')
                    $('#M1').append(errHead + result[1] + errEnd)
                if (result[2] != '')
                    $('#M2').append(errHead + result[2] + errEnd)
                if (result[3] != '')
                    $('#M3').append(errHead + result[3] + errEnd)
            }
        },
        complete: function () {
        },
        error: function () {
        }
    })
})

$("#SearchShopListbtn").bind("click", function () {
    const form = document.forms["ShopSelect"];
    const Shop = form.elements.Shop.value;
    const City = form.elements.City.value;
    const LowPrice = form.elements.LowPrice.value;
    const HighPrice = form.elements.HighPrice.value;
    const Amount = form.elements.Amount.value;
    const WorkOnly = $('#WorkOnly').prop('checked');
    var data = {
        Shop: Shop,
        City: City,
        LowPrice: LowPrice,
        HighPrice: HighPrice,
        Amount: Amount,
        WorkOnly: WorkOnly
    }
    $.ajax({
        url: '/_searchShopList',
        type: 'GET',
        data: data,
        beforeSend: function () {
            $("table").remove('#searchShopData');
        },
        success: function (result) {
            var insertText = '<table class="table" id="searchShopData"><thead>';
            insertText += '<tr><td>Shop</td>\
            <td>City</td>\
            <td>Mask Price</td>\
            <td>Mask Amount</td>\
            <td></td>\
            </tr></thead>';
            for (var i = 0; i < result.data.length; i++) {
                insertText += '<tr>';
                for (var j = 0; j < result.data[i].length; j++) {
                    insertText += '<td>';
                    insertText += result.data[i][j];
                    insertText += '</td>';
                }
                insertText += '<td><input type="text" name="Amount" id="_';
                insertText += result.data[i][0];
                insertText += '"/><button type="button" class="OrderBtn" id="';
                insertText += result.data[i][0];
                insertText += '">Buy!</button></td></tr>';
            }
            insertText += '</table>';

            $('#searchShopWrap').append(insertText);
        },
        complete: function () {
        },
        error: function () {
        }
    })
})

$("#SearchMyOrderbtn").bind("click", function () {
    const form = document.forms["OrderSelect"];
    const Status = form.elements.Status.value;
    var data = {
        Status: Status
    }
    $.ajax({
        url: '/_searchMyOrderList',
        type: 'GET',
        data: data,
        beforeSend: function () {
            $("table").remove('#searchWrapData');
        },
        success: function (result) {
            var insertText = '<table class="table" id="searchWrapData"><thead>';
            insertText += '<tr><td>OID</td>\
            <td>Status</td>\
            <td>Start</td>\
            <td>End</td>\
            <td>Shop</td>\
            <td>Total Price</td>\
            <td>Action</td>\
            </tr></thead>';
            for (var i = 0; i < result.data.length; i++) {
                insertText += '<tr><td>';
                if (result.data[i][1] == "Not Finished") {
                    insertText += '<label class="switch"><input type="checkbox" class="chkboxName" id="';
                    insertText += result.data[i][0] + '"value="' + result.data[i][0];
                    insertText += '"></label>';
                }
                insertText += result.data[i][0];
                insertText += '</td>';
                for (var j = 1; j < result.data[i].length; j++) {
                    insertText += '<td>';
                    insertText += result.data[i][j];
                    insertText += '</td>';
                }
                insertText += '<td><button type="button" class="DelOrderBtn" id="';
                insertText += result.data[i][0];
                insertText += '">X</button></td></tr>';
            }
            insertText += '</table>';

            $('#searchWrap').append(insertText);
        }
    })
})

$("#SearchShopOrderbtn").bind("click", function () {
    const form = document.forms["OrderSelect"];
    const Status = form.elements.Status.value;
    const Shop = form.elements.Shop.value;
    var data = {
        Status: Status,
        Shop: Shop
    }
    $.ajax({
        url: '/_searchShopOrderList',
        type: 'GET',
        data: data,
        beforeSend: function () {
            $("table").remove('#searchWrapData');
        },
        success: function (result) {
            var insertText = '<table class="table" id="searchWrapData"><thead>';
            insertText += '<tr><td>OID</td>\
            <td>Status</td>\
            <td>Start</td>\
            <td>End</td>\
            <td>Shop</td>\
            <td>Total Price</td>\
            <td>Action</td>\
            </tr></thead>';
            for (var i = 0; i < result.data.length; i++) {
                insertText += '<tr><td>';
                if (result.data[i][1] == "Not Finished") {
                    insertText += '<label class="switch"><input type="checkbox" class="chkboxName" id="';
                    insertText += result.data[i][0] + '"value="' + result.data[i][0];
                    insertText += '"></label>';
                }
                insertText += result.data[i][0];
                insertText += '</td>';
                for (var j = 1; j < result.data[i].length; j++) {
                    insertText += '<td>';
                    insertText += result.data[i][j];
                    insertText += '</td>';
                }
                if (result.data[i][1] == "Not Finished") {

                    insertText += '<td><button type="button" class="DoneOrderBtn" id="';
                    insertText += result.data[i][0];
                    insertText += '">Done</button><button type="button" class="DelOrderBtn" id="';
                    insertText += result.data[i][0];
                    insertText += '">X</button></td>';
                }
                insertText += '</tr>';
            }
            insertText += '</table>';
            $('#searchWrap').append(insertText);
        }
    })
})

$("#searchWrap").on("click", ".DelOrderBtn", function () {
    var data = {
        OID: this.id
    }
    $.ajax({
        url: '/_DelOrder',
        type: 'GET',
        data: data,
        beforeSend: function () {
        },
        success: function (result) {
            alert(result.data)
            location.reload();
        },
        complete: function () {
        },
        error: function () {
        }
    })
})
$("#searchWrap").on("click", ".DoneOrderBtn", function () {
    var data = {
        OID: this.id
    }
    $.ajax({
        url: '/_DoneOrder',
        type: 'GET',
        data: data,
        beforeSend: function () {
        },
        success: function (result) {
            alert(result.data)
            location.reload();
        },
        complete: function () {
        },
        error: function () {
        }
    })
})
$(".DoneAllOrderBtn").bind("click", function () {
    var checkboxesChecked = "";
    $("input[type=checkbox]:checked").each(function() {
        checkboxesChecked+=($(this).val());
        checkboxesChecked+=" ";
    });
    var data = {
        OIDs: checkboxesChecked
    }
    $.ajax({
        url: '/_DoneAllOrder',
        type: 'GET',
        data: data,
        beforeSend: function () {
        },
        success: function (result) {
            alert(result.data)
            location.reload();
        },
        complete: function () {
        },
        error: function () {
        }
    })
})
$(".DelAllOrderBtn").bind("click", function () {
    var checkboxesChecked = "";
    $("input[type=checkbox]:checked").each(function() {
        checkboxesChecked+=($(this).val());
        checkboxesChecked+=" ";
    });
    var data = {
        OIDs: checkboxesChecked
    }
    $.ajax({
        url: '/_DelAllOrder',
        type: 'GET',
        data: data,
        beforeSend: function () {
        },
        success: function (result) {
            alert(result.data)
            location.reload();
        },
        complete: function () {
        },
        error: function () {
        }
    })
})
$("#searchShopWrap").on("click", ".OrderBtn", function () {
    var data = {
        Shop: this.id,
        Amount: document.getElementById('_' + this.id).value
    }
    $.ajax({
        url: '/_Order',
        type: 'GET',
        data: data,
        beforeSend: function () {
        },
        success: function (result) {
            alert(result.data)
            location.reload();
        },
        complete: function () {
        },
        error: function () {
        }
    })
})

$("#RegisterShopBtn").bind("click", function () {
    const form = document.forms["RegisterShop"];
    const Shop = form.elements.Shop.value;
    const City = form.elements.City.value;
    const Price = form.elements.Price.value;
    const Amount = form.elements.Amount.value;
    var data = {
        Shop: Shop,
        City: City,
        Price: Price,
        Amount: Amount
    }
    errHead = '<nobr id="errMsg">';
    errEnd = '</nobr>';
    $.ajax({
        url: '/_registerShop',
        type: 'GET',
        data: data,
        beforeSend: function () {
            $("nobr").remove('#errMsg');
        },
        success: function (result) {
            if (result[0] == 'Register Success') {
                alert(result[0]);
                location.reload();
            }
            else {
                if (result[0] != '')
                    $('#M0').append(errHead + result[0] + errEnd)
                if (result[1] != '')
                    $('#M1').append(errHead + result[1] + errEnd)
                if (result[2] != '')
                    $('#M2').append(errHead + result[2] + errEnd)
                if (result[3] != '')
                    $('#M3').append(errHead + result[3] + errEnd)
            }
        },
        complete: function () {
        },
        error: function () {
        }
    })
})

$("#AddEmployee").bind("click", function () {
    const form = document.forms["AddEmployee"];
    const Employee = form.elements.Employee.value;
    var data = {
        Employee: Employee
    }
    $.ajax({
        url: '/_AddEmployee',
        type: 'GET',
        data: data,
        beforeSend: function () {
        },
        success: function (result) {
            alert(result.data)
            location.reload();
        },
        complete: function () {
        },
        error: function () {
        }
    })
})

$(".DelEmployeeBtn").bind("click", function () {
    var data = {
        Employee: this.id
    }
    $.ajax({
        url: '/_DelEmployee',
        type: 'GET',
        data: data,
        beforeSend: function () {
        },
        success: function (result) {
            alert(result.data)
            location.reload();
        },
        complete: function () {
        },
        error: function () {
        }
    })
})

$("#PriceChange").bind("click", function () {
    const form = document.forms["PriceChange"];
    const Price = form.elements.Price.value;
    var data = {
        Price: Price
    }
    $.ajax({
        url: '/_PriceChange',
        type: 'GET',
        data: data,
        beforeSend: function () {
        },
        success: function (result) {
            alert(result.data)
        },
        complete: function () {
        },
        error: function () {
        }
    })
})

$("#AmountChange").bind("click", function () {
    const form = document.forms["AmountChange"];
    const Amount = form.elements.Amount.value;
    var data = {
        Amount: Amount
    }
    $.ajax({
        url: '/_AmountChange',
        type: 'GET',
        data: data,
        beforeSend: function () {
        },
        success: function (result) {
            alert(result.data)
        },
        complete: function () {
        },
        error: function () {
        }
    })
})
