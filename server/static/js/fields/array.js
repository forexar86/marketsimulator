/**
 * Field of array type 
 * @param {list<Field>} s -- array of fields (of scalar, array or object type)
 */

function ArrayValue(s, root) {
	var self = this;
	self.array = function () { return true; }
	
	var fields = map(s, function (x,i) {
						return new Property("", x, true, self);
				});
				
	self._storage = ko.observableArray(fields);
	
	/**
	 *	Removes an element from the array 
	 */
	self.remove = function (element) {
		self._storage.remove(element);
	}

	/**
	 * 	Returns true iff element can be removed from array
	 */
	self.canBeRemoved = ko.computed(function () {
		return self._storage().length > 1;
	})
		
	/**
	 *	Duplicates an element in the array 
	 */
	self.duplicate = function (element) {
		self._storage.push(element.clone());
	}
	
	/**
	 *	Elements of the array 
	 */				
	self.elements = ko.computed(function () {
		return self._storage();
	})
	
	/**
	 *	Returns true if the fields has been changed 
	 */
	self.hasChanged = function () { 
		return any(self.elements(), function (e) {
			return e.hasChanged();
		}); 
	}
	
	/**
	 *	Clones array field 
	 */
	self.clone = function () {
		return new ArrayValue(map(s, function (x) { return x.clone(); }));
	}

	/**
	 *  Returns serialized representation of the field 
	 */
	self.serialized = function () {
		return map(self.elements(), function (property) {
			return property.impl().serialized();
		});
	}
	
	self.dropHistory = function () {
		foreach(self.elements(), function (e) {
			e.dropHistory();
		})
	}
	
	/**
	 *  For the moment we consider all arrays as value types  
	 */
	self.isReference = function () { return false; }

	/**
	 *  Returns true iff any child has an error 
	 */
	self.hasError = ko.computed(function () {
		return any(self._storage(), function (x) { return x.impl().hasError(); })
	})

	/**
	 *  expanded representation of the array 
	 */
	self.expanded = self._storage;
}

