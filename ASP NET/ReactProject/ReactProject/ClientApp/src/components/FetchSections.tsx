import * as React from 'react';
import { connect } from 'react-redux';
import { RouteComponentProps } from 'react-router';
import { Link } from 'react-router-dom';
import { ApplicationState } from '../store';
import * as SectionsStore from '../store/Sections';

// At runtime, Redux will merge together...
type SectionProps =
    SectionsStore.SectionsState // ... state we've requested from the Redux store
    & typeof SectionsStore.actionCreators // ... plus action creators we've requested
    & RouteComponentProps<{ sectionIdIndex: string }>; // ... plus incoming routing parameters


class FetchData extends React.PureComponent<SectionProps> {
    // This method is called when the component is first added to the document
    public componentDidMount() {
        this.ensureDataFetched();
    }

    // This method is called when the route parameters change
    public componentDidUpdate() {
        this.ensureDataFetched();
    }

    public render() {
        return (
            <React.Fragment>
                <h1 id="tabelLabel">List of Sections</h1>
                <p>This component demonstrates fetching data from the server and working with URL parameters.</p>
                {this.renderSectionsTable()}
                {this.renderPagination()}
            </React.Fragment>
        );
    }

    private ensureDataFetched() {
        const sectionIdIndex = parseInt(this.props.match.params.sectionIdIndex, 10) || 0;
        this.props.requestSections(sectionIdIndex);
    }

    private renderSectionsTable() {
        return (
            <table className='table table-striped' aria-labelledby="tabelLabel">
                <thead>
                    <tr>
                        <th>Section ID</th>
                        <th>Section Name</th>
                    </tr>
                </thead>
                <tbody>
                    {this.props.sections.map((dept: SectionsStore.Section) =>
                        <tr key={dept.sectionId}>
                            <td>{dept.sectionId}</td>
                            <td>{dept.sectionName}</td>
                        </tr>
                    )}
                </tbody>
            </table>
        );
    }

    private renderPagination() {
        const prevSectionIdIndex = (this.props.sectionIdIndex || 0) - 5;
        const nextSectionIdIndex = (this.props.sectionIdIndex || 0) + 5;

        return (
            <div className="d-flex justify-content-between">
                <Link className='btn btn-outline-secondary btn-sm' to={`/fetch-section/${prevSectionIdIndex}`}>Previous</Link>
                {this.props.isLoading && <span>Loading...</span>}
                <Link className='btn btn-outline-secondary btn-sm' to={`/fetch-section/${nextSectionIdIndex}`}>Next</Link>
            </div>
        );
    }
}

export default connect(
    (state: ApplicationState) => state.sections, // Selects which state properties are merged into the component's props
    SectionsStore.actionCreators                // Selects which action creators are merged into the component's props
)(FetchData as any); // eslint-disable-line @typescript-eslint/no-explicit-any