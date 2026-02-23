# questionnaire.QTCIVALQQ96

> Intravascular Access Lines : Peripheral IV Assessment

**Schema:** questionnaire
**Columnas:** 8
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Intravascular Access Lines : Peripheral IV Assessment

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q96Q1 | varchar |  |  | SI | Need Assessment	 |
| Q96Q2 | varchar |  |  | SI | Care |
| Q96Q3 | varchar |  |  | SI | Site Details	 |
| Q96Q4 | varchar |  |  | SI | Dressing Type / Appearance	 |
| Q96Q5 | varchar |  |  | SI | Peripheral IV Patency	 |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*