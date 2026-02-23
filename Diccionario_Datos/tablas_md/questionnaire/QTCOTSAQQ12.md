# questionnaire.QTCOTSAQQ12

**Schema:** questionnaire
**Columnas:** 10
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Cuestionario/Formulario**. Plantilla de evaluación clínica estructurada.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | varchar | PK |  | NO | - |
| Q12Q1 | varchar | PK |  | SI | Substance trialled |
| Q12Q2 | varchar | PK |  | SI | Amount |
| Q12Q3 | varchar | PK |  | SI | Strategies / Manoeuvres comments and response |
| Q12Q4 | varchar | PK |  | SI | Pre oral stage |
| Q12Q5 | varchar | PK |  | SI | Oral stage |
| Q12Q6 | varchar | PK |  | SI | Pharyngeal stage |
| Q12Q7 | varchar | PK |  | SI | Oesophageal stage |
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| childsub | bigint | PK |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*