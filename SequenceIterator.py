class SequenceIterator:
    """An iterator for any of Python's sequence types."""

    def __init__(self, sequencer):
        """Create an iterator for the given sequence."""
        self._seq = sequencer    # keep a refernce to the underlying data
        self._k = -1             # will increment to 0 on first call to next

    def __next__(self):
        """Return the next element, or else raise StopIteration error."""
        self._k += 1    # advance to next index
        if self._k < len(self._seq):
            return(self._seq[self._k])   # return the data element
        else:
            raise StopIteration()        # there are no more elements


    def __iter__(self):
        """By  convention, an iterator must return itself as an iterator."""
        return self
     