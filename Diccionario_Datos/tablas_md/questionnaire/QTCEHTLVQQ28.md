# questionnaire.QTCEHTLVQQ28

> Formulario de Envío de Muestras para HTLV I/II : Tecnica Realizada

**Schema:** questionnaire
**Columnas:** 9
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Formulario de Envío de Muestras para HTLV I/II : Tecnica Realizada

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q28Q1 | numeric |  |  | SI | N° Tamizaje |
| Q28Q2 | varchar |  |  | SI | Técnica |
| Q28Q3 | varchar |  |  | SI | Lote |
| Q28Q4 | varchar |  |  | SI | CUT-OFF |
| Q28Q5 | varchar |  |  | SI | Reactividad |
| Q28Q6 | varchar |  |  | SI | Resultado |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*