# questionnaire.QTCEACCMORQQ26

> Denuncia Accidente por Mordeduras : Tratamiento

**Schema:** questionnaire
**Columnas:** 6
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Denuncia Accidente por Mordeduras : Tratamiento

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q26Q1 | varchar |  |  | SI | Dosis |
| Q26Q2 | date |  |  | SI | Fecha Prevista |
| Q26Q3 | date |  |  | SI | Fecha Efectiva |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*