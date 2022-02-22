"use strict";
var __extends = (this && this.__extends) || (function () {
    var extendStatics = function (d, b) {
        extendStatics = Object.setPrototypeOf ||
            ({ __proto__: [] } instanceof Array && function (d, b) { d.__proto__ = b; }) ||
            function (d, b) { for (var p in b) if (Object.prototype.hasOwnProperty.call(b, p)) d[p] = b[p]; };
        return extendStatics(d, b);
    };
    return function (d, b) {
        if (typeof b !== "function" && b !== null)
            throw new TypeError("Class extends value " + String(b) + " is not a constructor or null");
        extendStatics(d, b);
        function __() { this.constructor = d; }
        d.prototype = b === null ? Object.create(b) : (__.prototype = b.prototype, new __());
    };
})();
Object.defineProperty(exports, "__esModule", { value: true });
var React = require("react");
var react_redux_1 = require("react-redux");
var react_router_dom_1 = require("react-router-dom");
var SectionsStore = require("../store/Sections");
var FetchData = /** @class */ (function (_super) {
    __extends(FetchData, _super);
    function FetchData() {
        return _super !== null && _super.apply(this, arguments) || this;
    }
    // This method is called when the component is first added to the document
    FetchData.prototype.componentDidMount = function () {
        this.ensureDataFetched();
    };
    // This method is called when the route parameters change
    FetchData.prototype.componentDidUpdate = function () {
        this.ensureDataFetched();
    };
    FetchData.prototype.render = function () {
        return (React.createElement(React.Fragment, null,
            React.createElement("h1", { id: "tabelLabel" }, "List of Sections"),
            React.createElement("p", null, "This component demonstrates fetching data from the server and working with URL parameters."),
            this.renderSectionsTable(),
            this.renderPagination()));
    };
    FetchData.prototype.ensureDataFetched = function () {
        var sectionIdIndex = parseInt(this.props.match.params.sectionIdIndex, 10) || 0;
        this.props.requestSections(sectionIdIndex);
    };
    FetchData.prototype.renderSectionsTable = function () {
        return (React.createElement("table", { className: 'table table-striped', "aria-labelledby": "tabelLabel" },
            React.createElement("thead", null,
                React.createElement("tr", null,
                    React.createElement("th", null, "Section ID"),
                    React.createElement("th", null, "Section Name"))),
            React.createElement("tbody", null, this.props.sections.map(function (dept) {
                return React.createElement("tr", { key: dept.sectionId },
                    React.createElement("td", null, dept.sectionId),
                    React.createElement("td", null, dept.sectionName));
            }))));
    };
    FetchData.prototype.renderPagination = function () {
        var prevSectionIdIndex = (this.props.sectionIdIndex || 0) - 5;
        var nextSectionIdIndex = (this.props.sectionIdIndex || 0) + 5;
        return (React.createElement("div", { className: "d-flex justify-content-between" },
            React.createElement(react_router_dom_1.Link, { className: 'btn btn-outline-secondary btn-sm', to: "/fetch-section/".concat(prevSectionIdIndex) }, "Previous"),
            this.props.isLoading && React.createElement("span", null, "Loading..."),
            React.createElement(react_router_dom_1.Link, { className: 'btn btn-outline-secondary btn-sm', to: "/fetch-section/".concat(nextSectionIdIndex) }, "Next")));
    };
    return FetchData;
}(React.PureComponent));
exports.default = (0, react_redux_1.connect)(function (state) { return state.sections; }, // Selects which state properties are merged into the component's props
SectionsStore.actionCreators // Selects which action creators are merged into the component's props
)(FetchData); // eslint-disable-line @typescript-eslint/no-explicit-any
//# sourceMappingURL=FetchSections.js.map