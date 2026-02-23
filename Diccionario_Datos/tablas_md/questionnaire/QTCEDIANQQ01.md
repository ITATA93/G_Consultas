# questionnaire.QTCEDIANQQ01

**Schema:** questionnaire
**Columnas:** 5
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Cuestionario/Formulario**. Plantilla de evaluación clínica estructurada.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | varchar | PK |  | NO | - |
| Q01Q1 | varchar | PK |  | SI | Ubicación |
| Q01Q2 | varchar | PK |  | SI | N° |
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| childsub | bigint | PK |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*