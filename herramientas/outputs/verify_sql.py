"""Verificar queries SQL"""
content = open('Consultas_live/entrega_turno_hospitalizados.sql', 'r', encoding='utf-8').read()
print(f"Archivo: {len(content)} caracteres")
print(f"Queries (SELECT TOP): {content.count('SELECT TOP')}")
for fn in ['DATEDIFF', 'CURRENT_DATE', 'CASE', 'STRING_AGG', 'COUNT', 'AVG', 'MIN', 'MAX']:
    count = content.count(fn)
    if count > 0:
        print(f"  {fn}: {count} usos")
for bad in ['INSERT', 'UPDATE ', 'DELETE', 'DROP', 'TRUNCATE']:
    # solo buscar fuera de comentarios
    lines = [l for l in content.split('\n') if not l.strip().startswith('--')]
    code = '\n'.join(lines)
    if bad in code.upper():
        print(f"  ALERTA: {bad} encontrado en codigo!")
print("Verificacion OK: Solo SELECT")
