# questionnaire.QTCEPLANTCQQ09

> Plan de Tratamiento Consensuado : Acuerdos y Responsables de cada intervención:

**Schema:** questionnaire
**Columnas:** 5
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Plan de Tratamiento Consensuado : Acuerdos y Responsables de cada intervención:

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q09Q1 | varchar |  |  | SI | Acuerdos  |
| Q09Q2 | varchar |  |  | SI | Responsables  |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*