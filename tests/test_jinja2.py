import pytest
import os.path



def test_archive(mkdocs_site, tmpdir):
    p  = os.path.join(
        tmpdir,
        'archive',
        'index.html'
    )

    assert os.path.exists(p)

    expected = '''<p></p>
<p>
  <h3>2020</h3>
  
    <h4>January</h4>
    
      
      <a href="/2020/01/third/">Third</a>
      <br />
    
  </p>
<p>
  <h3>2019</h3>
  
    <h4>June</h4>
    
      
      <a href="/2019/06/first/">First</a>
      <br />
    
  
    <h4>September</h4>
    
      
      <a href="/2019/09/second/">Second</a>
      <br />
    
  </p>
<p></p>'''

    with open(p, 'r') as f:
        content = f.read()
        assert expected in content



def test_recent(mkdocs_site, tmpdir):
    p  = os.path.join(
        tmpdir,
        'recent',
        'index.html'
    )

    assert os.path.exists(p)

    expected = '''<p>
  
  
  <a href="2020/01/third/">
  Third
  </a>
  <br />

  
  
  <a href="2019/09/second/">
  Second
  </a>
  <br />

  
  
  <a href="2019/06/first/">
  First
  </a>
  <br />
</p>'''

    with open(p, 'r') as f:
        content = f.read()
        assert expected in content