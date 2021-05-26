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
            if (result[0] == 'Register success!'){
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
        WorkOnly:WorkOnly
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
            </tr></thead>';
            for (var i = 0; i < result.data.length; i++) {
                insertText += '<tr>';
                for (var j = 0; j < result.data[i].length; j++) {
                    insertText += '<td>';
                    insertText += result.data[i][j];
                    insertText += '</td>';
                }
                insertText += '</tr>';
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
            if (result[0] == 'Register Success'){
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

/*
$("#stockdatebtn").bind("click", function () {
    const form = document.forms["stock"];
    const year = form.elements.year.value;
    const month = form.elements.month.value;
    const day = form.elements.day.value;
    var date = year + '/' + month + '/' + day;
    var data = {
        Date: date
    }
    $.ajax({
        url: '/_stockdate',
        type: 'GET',
        data: data,
        beforeSend: function () {
            $("table").remove('#stockdatedata');
            $("table").remove('#historydata');
            $("#stockdatebtn").attr({ disabled: "disabled" });
        },
        success: function (result) {
            var insertText = '<table class="table" id="stockdatedata"><thead>';
            insertText += '<tr>';
            for (var i = 0; i < result.Header.length; i++) {
                insertText += '<td>';
                insertText += result.Header[i];
                insertText += '</td>';
            }
            insertText += '</tr></thead>';

            for (var i = 0; i < result.Data.length; i++) {
                insertText += '<tr>';
                for (var j = 0; j < result.Data[i].length; j++) {
                    insertText += '<td>';
                    insertText += result.Data[i][j];
                    insertText += '</td>';
                }
                insertText += '</tr>';
            }
            insertText += '</table>';

            $('#stockdate').append(insertText);
        },
        complete: function () {
            $("#stockdatebtn").removeAttr("disabled");
        },
        error: function (result) {
            alert("Error.\nMaybe you have closed the app or have a illegal query to database.\nPlease check the status.");
        }
    })

    $.ajax({
        url: '/_history',
        type: 'GET',
        data: data,
        beforeSend: function () {
            //
        },
        success: function (result) {
            var insertText = '<table class="table" id="historydata"><thead>';
            insertText += '<tr>';
            for (var i = 0; i < result.Header.length; i++) {
                insertText += '<td>';
                insertText += result.Header[i];
                insertText += '</td>';
            }
            insertText += '</tr></thead>';

            for (var i = result.Data.length - 1; i >= result.Data.length - 5 && i >= 0; i--) {
                insertText += '<tr>';
                for (var j = 0; j < result.Data[i].length; j++) {
                    insertText += '<td>';
                    insertText += result.Data[i][j];
                    insertText += '</td>';
                }
                insertText += '</tr>';
            }
            insertText += '</table>';

            $('#history').append(insertText);
        },
        complete: function () {
            //$("#stockdatebtn").removeAttr("disabled");
        },
        error: function (result) {
            alert("Error.\nMaybe you have closed the app or have a illegal query to database.\nPlease check the status.");
        }
    })

})

$("#historydelbtn").bind("click", function () {
    var data = {}
    $.ajax({
        url: '/_historydel',
        type: 'GET',
        data: data,
        beforeSend: function () {
            $("table").remove('#historydata');
            $("#historydelbtn").attr({ disabled: "disabled" });
        },
        success: function (result) {
            var insertText = '<table class="table" id="historydata"><thead>';
            insertText += '<tr>';
            for (var i = 0; i < result.Header.length; i++) {
                insertText += '<td>';
                insertText += result.Header[i];
                insertText += '</td>';
            }
            insertText += '</tr></thead>';

            for (var i = result.Data.length - 1; i < result.Data.length - 5 && i >= 0; i++) {
                insertText += '<tr>';
                for (var j = 0; j < result.Data[i].length; j++) {
                    insertText += '<td>';
                    insertText += result.Data[i][j];
                    insertText += '</td>';
                }
                insertText += '</tr>';
            }
            insertText += '</table>';

            $('#history').append(insertText);
        },
        complete: function () {
            $("#historydelbtn").removeAttr("disabled");
        },
        error: function (result) {
            alert("Error.\nMaybe you have closed the app or have a illegal query to database.\nPlease check the status.");
        }
    })
})

$("#regionRatebtn").bind("click", function () {
    const form = document.forms["regionRate"];
    const region = form.elements.region.value;
    var data = {
        Region: region
    }
    $.ajax({
        url: '/_regionRate',
        type: 'GET',
        data: data,
        beforeSend: function () {
            //$("div").remove('#regionRatedata');
            //$("#regionRate").append('<div id="regionRatedata"></div>');
            $("#regionRatedatabtn").attr({ disabled: "disabled" });
        },
        success: function (result) {
            var chart = c3.generate({
                bindto: '#regionRatedata',
                data: {
                    x: 'Date',
                    xFormat: '%Y/%m',
                    rows: result.Data,
                    axes: {
                        rate: 'y',
                        Dow_Adj_Close_rate: 'y2'
                    }
                },
                axis: {
                    x: {
                        type: 'timeseries',
                        tick: {
                            format: '%Y/%m'
                        }
                    },
                    y2: {
                        show: true
                    }
                }
            });
        },
        complete: function () {
            $("#regionRatedatabtn").removeAttr("disabled");
        },
        error: function (result) {
            alert("Error.\nMaybe you have closed the app or have a illegal query to database.\nPlease check the status.");
        }

    })

})
*/