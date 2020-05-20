import { connect } from 'react-redux';
import { setExpandNode } from '../../action';
import DataDictionaryTable from './DataDictionaryTable';

const ReduxDataDictionaryTable = (() => {
  const mapStateToProps = state => ({
    dictionary: state.submission.dictionary,
    highlightingNodeID: state.ddgraph.tableExpandNodeID,
    dictionaryName: "Dictionary Utils Viz",
  });

  const mapDispatchToProps = dispatch => ({
    onExpandNode: nodeID =>
      dispatch(setExpandNode(nodeID)),
  });

  return connect(mapStateToProps, mapDispatchToProps)(DataDictionaryTable);
})();

export default ReduxDataDictionaryTable;
