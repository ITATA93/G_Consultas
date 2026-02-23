# questionnaire.QTCECONFAMQQ11

> Consejería Familiar : Consejería Familiar

**Schema:** questionnaire
**Columnas:** 9
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Consejería Familiar : Consejería Familiar

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q11Q1 | varchar |  |  | SI | Temas Prioritarios |
| Q11Q2 | varchar |  |  | SI | Registro de la Actividad |
| Q11Q3 | varchar |  |  | SI | Registrado por |
| Q11Q4 | date |  |  | SI | Fecha |
| Q11Q5 | time |  |  | SI | Hora |
| Q11Q6 | varchar |  |  | SI | CESFAM |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*