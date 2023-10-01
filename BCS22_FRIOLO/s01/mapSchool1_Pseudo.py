#    						                                    Start
#                                                                    |
#    			                            Initialize distances and previous_loc dictionaries.
#                                                                    |
#    				                                    Set distances[start] to 0.
#                                                                    |
#    			                            Initialize the visited set and shortpath_graph list.
#                                                                    |
#    			                            While visited is not equal to all locations in the graph:(Inside Below)
#                                                    |                                     |
#        			                                 |            Find the node with the minimum distance that is not in visited.
#                                                    |                                     |
#        			                                 |             Add the current node to the visited set.
#                                                    |                                     |
#        			                                 |             For each neighbor node of the current node:
#                                                    |                                     |
#            			                             |             Calculate the new distance.
#                                                    |                                     |
#            			                             |             If the new distance is less than distances[next_loc]:
#                                                    |                                     |
#               	 		                         |             Update distances[next_loc].
#                                                    |                                     |
#                		                             |             Update previous_loc[next_loc].
#                                                    |
#    				                            While end is not equal to start:(Inside Below)
#                                                    |                               |
#        			                                 |             Append end to the shortpath_graph.
#                                                    |                               |
#        			                                 |             Update end to previous_loc[end].
#                                                    |                               |
#        		                                     |            If start is equal to end, append start to the shortpath_graph.
#                                                    |
#    					                            Reverse the shortpath_graph.
#                                                                     |
#    		                Print "The shortest path from home to school (L to R):", followed by the contents of shortpath_graph.
#
#  						                                        End.