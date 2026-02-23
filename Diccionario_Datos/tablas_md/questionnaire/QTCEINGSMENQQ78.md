# questionnaire.QTCEINGSMENQQ78

> Ingreso Médico Salud Mental : Funcionamiento Cognitivo

**Schema:** questionnaire
**Columnas:** 6
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Ingreso Médico Salud Mental : Funcionamiento Cognitivo

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q78Q1 | varchar |  |  | SI | Área |
| Q78Q2 | varchar |  |  | SI | Evaluación |
| Q78Q3 | varchar |  |  | SI | Comentarios (Texto libre) |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*